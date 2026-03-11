package pedestria.fourcorners.client;

import net.minecraftforge.api.distmarker.Dist;
import net.minecraft.client.gui.screens.MenuScreens;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.event.lifecycle.FMLClientSetupEvent;
import pedestria.fourcorners.FourCorners;
import pedestria.fourcorners.client.screen.CoreFabricatorScreen;
import pedestria.fourcorners.client.screen.DimensionAccessorScreen;
import pedestria.fourcorners.registry.FCMenus;

@Mod.EventBusSubscriber(modid = FourCorners.MODID, bus = Mod.EventBusSubscriber.Bus.MOD, value = Dist.CLIENT)
public final class FCClientSetup {
    private FCClientSetup() {}

    @SubscribeEvent
    public static void registerScreens(FMLClientSetupEvent event) {
        event.enqueueWork(
                () -> {
                    MenuScreens.register(
                            FCMenus.DIMENSION_ACCESSOR_MENU.get(), DimensionAccessorScreen::new);
                    MenuScreens.register(
                            FCMenus.CORE_FABRICATOR_MENU.get(), CoreFabricatorScreen::new);
                });
    }
}
